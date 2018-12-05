import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

input_size = 9
output_size = 9
cell_size = 200
batch_size = 50
time_steps = 120
LR = 0.005
keep_pro = 0.7


def redata(data):
    mean = np.mean(data)
    std = np.std(data)
    return [(i - mean) / std for i in data]


data = pd.read_csv('/users/barry/desktop/DATA_BTC.csv')
date = data['DATE']
date = pd.to_datetime(date)
data['DATA'] = date

btc_usd = redata(data['BTC/USD'])
t_volume = redata(data['BTC_TRANS_VLOUME'])
m_diff = redata(data['mining_diff'])
hash = redata(data['hash_rate'])
effr = redata(data['EFFR'])
usd_num = redata(data['USD_supply'])
trend = redata(data['google_trend'])
gold = redata(data['GOLD'])
lite = redata(data['litecoin'])
database = []
for i in range(len(btc_usd)):
    database.append([float(btc_usd[i]), float(t_volume[i]), float(m_diff[i]), float(hash[i]), float(effr[i]),
                     float(usd_num[i]), float(trend[i]), float(gold[i]), float(lite[i])])


def predata(data, seq_len):
    sequence_length = seq_len + 1
    result = []
    for i in range(len(data) - sequence_length):
        result.append(data[i: i + sequence_length])

    result = np.array(result)

    row = round(0.8 * result.shape[0])
    train = result[:int(row), :]
    np.random.shuffle(train)

    x_train = train[:, :-1, :]
    y_train = train[:, 1:, :]
    x_test = result[int(row):, :-1, :]
    y_test = result[int(row):, 1:, :]

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], x_train.shape[2]))
    y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[1], y_train.shape[2]))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], x_test.shape[2]))
    y_test = np.reshape(y_test, (y_test.shape[0], y_test.shape[1], x_test.shape[2]))

    return [x_train, y_train, x_test, y_test]


def getbatch():
    global x_train, y_train, x_test, y_test
    length = len(x_train)
    counter = 0
    randlist = []
    train_in = []
    train_out = []
    while counter < batch_size:
        index = np.random.randint(0, length - 1)
        if index not in randlist:
            train_in.append(x_train[index])
            train_out.append(y_train[index])
            randlist.append(index)
            counter += 1
    train_in = np.reshape(train_in, (batch_size, time_steps, input_size))
    train_out = np.reshape(train_out, (batch_size, time_steps, input_size))

    length = len(x_test)
    counter = 0
    randlist = []
    test_in = []
    test_out = []
    while counter < batch_size:
        index = np.random.randint(0, length - 1)
        if index not in randlist:
            test_in.append(x_test[index])
            test_out.append(y_test[index])
            randlist.append(index)
            counter += 1
    test_in = np.reshape(test_in, (batch_size, time_steps, input_size))
    test_out = np.reshape(test_out, (batch_size, time_steps, input_size))

    return [train_in, train_out, test_in, test_out]


def add_layer(x, in_size, out_size, act_fun=None):
    W = tf.Variable(tf.random_normal([in_size, out_size]))
    b = tf.Variable(tf.random_normal([out_size]))
    y = tf.matmul(x, W) + b
    y = tf.nn.dropout(y, keep_prob=keep_pro)
    if act_fun is None:
        return y
    else:
        y = act_fun(y)
        return y


if __name__ == '__main__':
    x_train, y_train, x_test, y_test = predata(database, time_steps)
    train_in, train_out, test_in, test_out = getbatch()

    xs = tf.placeholder(tf.float32, [None, time_steps, input_size])
    ys = tf.placeholder(tf.float32, [None, time_steps, output_size])
    batch = tf.placeholder(tf.int32, [])

    # hidden input layer
    x_input_layer = tf.reshape(xs, [-1, input_size])

    y1_in = add_layer(x_input_layer, input_size, 10)
    y2_in = add_layer(y1_in, 10, 20, act_fun=tf.nn.relu)
    y3_in = add_layer(y2_in, 20, 30, act_fun=tf.nn.relu)
    y4_in = add_layer(y3_in, 30, cell_size, act_fun=tf.nn.relu)

    y_input_layer = y4_in
    y_input_layer = tf.reshape(y_input_layer, shape=[-1, time_steps, cell_size])
    # LSTM cell layer
    with tf.variable_scope('LSTM_layer'):
        lstm_cell_building = tf.contrib.rnn.BasicLSTMCell(cell_size, forget_bias=1.0, state_is_tuple=True)
    lstm_cell_dropout = tf.contrib.rnn.DropoutWrapper(lstm_cell_building, output_keep_prob=0.7)
    #    lstm_cell = [lstm_cell_dropout]
    #    for i in range(4):
    #        lstm_cell.append(lstm_cell_dropout)
    lstm_cell = tf.contrib.rnn.MultiRNNCell([lstm_cell_dropout for _ in range(4)])
    with tf.variable_scope('initial_state', reuse=True):
        cell_state = lstm_cell.zero_state(batch, dtype=tf.float32)
    with tf.variable_scope('RNN_operating'):
        cell_output, state = tf.nn.dynamic_rnn(lstm_cell, y_input_layer, initial_state=cell_state, time_major=False,
                                               scope=None)
    # hidden output layer
    # with tf.variable_scope('Output_layer_weight'):
    #    W_out = tf.get_variable(name='W_out', shape=[cell_size, output_size], dtype=tf.float32)
    # with tf.variable_scope('Output_layer_bias'):
    #    b_out = tf.get_variable(name='b_out', shape=[output_size], dtype=tf.float32)
    x_output_layer = tf.reshape(cell_output, [-1, cell_size])

    y1_out = add_layer(x_output_layer, cell_size, 20, act_fun=tf.nn.relu)
    y2_out = add_layer(y1_out, 20, output_size, act_fun=tf.nn.relu)
    # y3_out = add_layer(y2_out, 20, 10)
    # y4_out = add_layer(y3_out, 10 ,output_size)

    y_output_layer = y2_out
    prediction = tf.reshape(y_output_layer, shape=[-1, time_steps, output_size])

    # Loss computing

    # cross_entropy =tf.multiply(tf.square(tf.subtract( tf.reshape(prediction, [-1]) ,  tf.reshape(ys, [-1]) )), 0.5)

    # loss_finial = tf.reduce_mean(cross_entropy)
    loss1 = tf.losses.mean_squared_error(ys, prediction)
    loss2 = tf.losses.mean_squared_error(ys[:, :, 0], prediction[:, :, 0])
    loss_final = loss1 * 1 + loss2 * 0
    train = tf.train.GradientDescentOptimizer(LR).minimize(loss_final)
    # train = tf.train.AdamOptimizer(LR).minimize(loss_final)


    saver = tf.train.Saver()
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)

        for i in range(100):
            train_in, train_out, test_in, test_out = getbatch()
            train_result, loss = sess.run([train, loss_final],
                                          feed_dict={xs: train_in, ys: train_out, batch: batch_size})

            if i % 10 == 0:
                test_result, test_loss = sess.run([train, loss_final],
                                                  feed_dict={xs: test_in, ys: test_out, batch: batch_size})
                print('train loss:', loss, '  test loss', test_loss)

        path = '/users/barry/desktop/LSTM_CODE/model.ckpt'
        saver.save(sess, path)

    print('End')

    with tf.Session() as sess:
        saver.restore(sess, path)

        run_model = database[-time_steps:]
        run_model = np.reshape(run_model, (1, time_steps, input_size))
        for i in range(7):
            run_model = np.reshape(run_model, (1, time_steps, input_size))
            result = sess.run(prediction, feed_dict={xs: run_model, batch: 1})
            newday = result[0][-1]
            newday = np.reshape(newday, (-1, input_size))
            run_model = np.reshape(run_model, (-1, input_size))
            run_model = np.append(run_model, newday, axis=0)
            run_model = run_model[1:, :]


        run_model = run_model[:, 0]
        run_model = np.reshape(run_model, -1)
        output = run_model[-7:]
        mean = np.mean(data['BTC/USD'])
        std = np.std(data['BTC/USD'])
        output = [(i * std + mean) for i in output]
        print(output)