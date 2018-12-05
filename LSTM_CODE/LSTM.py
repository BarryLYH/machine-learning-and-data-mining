import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

input_size = 1
output_size = 1
cell_size = 40
batch_size = 200
time_steps = 100
LR = 0.005
keep_pro = 0.7


data = pd.read_csv('/users/barry/desktop/DATA_LSTM.csv')
date = data['Date']
date = pd.to_datetime(date)
data["Date"] = date
ts = pd.Series(data['Open'].values, index=data['Date'])
database = data['Open']
#database = np.log(database)
#database.dropna(inplace=True)

def predata(data, seq_len):
    sequence_length = seq_len + 1
    result = []
    for i in range(len(data) - sequence_length):
        result.append(data[i: i + sequence_length])

    result = np.array(result)

    row = round(0.9 * result.shape[0])
    train = result[:int(row), :]
    np.random.shuffle(train)

    x_train = train[:, :-1]
    y_train = train[:, 1:]
    x_test = result[int(row):, :-1]
    y_test = result[int(row):, 1:]

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    y_train = np.reshape(y_train, (y_train.shape[0], y_train.shape[1], 1))
    x_test  = np.reshape(x_test,  (x_test.shape[0], x_test.shape[1], 1))
    y_test  = np.reshape(y_test,  (y_test.shape[0], y_test.shape[1], 1))

    return [x_train, y_train, x_test, y_test]

def getbatch():
    global x_train, y_train, x_test, y_test
    length =  len(x_train)
    counter = 0
    randlist = []
    train_in = []
    train_out = []
    while counter<batch_size:
        index = np.random.randint(0, length-1)
        if index not in randlist:
            train_in.append(x_train[index])
            train_out.append(y_train[index])
            randlist.append(index)
            counter += 1

    length = len(x_test)
    counter = 0
    randlist = []
    test_in = []
    test_out = []
    while counter<batch_size:
        index = np.random.randint(0, length-1)
        if index not in randlist:
            test_in.append(x_test[index])
            test_out.append(y_test[index])
            randlist.append(index)
            counter += 1
    return [train_in, train_out, test_in, test_out]

def add_layer(x, in_size, out_size, act_fun = None):
    W = tf.Variable(tf.random_normal([in_size, out_size]))
    b = tf.Variable(tf.random_normal([out_size]))
    y = tf.matmul(x, W) + b
    y = tf.nn.dropout(y, keep_prob=keep_pro)
    if act_fun is None:
        return y
    else:
        y= act_fun(y)
        return y



if __name__=='__main__':
    x_train, y_train, x_test, y_test = predata(database, time_steps)
    train_in, train_out, test_in, test_out = getbatch()

    xs = tf.placeholder(tf.float32, [None, time_steps, input_size])
    ys = tf.placeholder(tf.float32, [None, time_steps, output_size])

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
    lstm_cell_dropout =  tf.contrib.rnn.DropoutWrapper(lstm_cell_building, output_keep_prob = 0.7)
    lstm_cell = tf.contrib.rnn.MultiRNNCell([lstm_cell_dropout]*3)
    with tf.variable_scope('initial_state'):
        cell_state = lstm_cell.zero_state(None, dtype=tf.float32)
    with tf.variable_scope('RNN_operating'):
        cell_output, state = tf.nn.dynamic_rnn(lstm_cell, y_input_layer, initial_state=cell_state, time_major=False,scope=None)
# hidden output layer
    #with tf.variable_scope('Output_layer_weight'):
    #    W_out = tf.get_variable(name='W_out', shape=[cell_size, output_size], dtype=tf.float32)
    #with tf.variable_scope('Output_layer_bias'):
    #    b_out = tf.get_variable(name='b_out', shape=[output_size], dtype=tf.float32)
    x_output_layer = tf.reshape(cell_output, [-1, cell_size])

    y1_out = add_layer(x_output_layer, cell_size, output_size, act_fun=tf.nn.relu)
    #y2_out = add_layer(y1_out, 2, output_size, act_fun=tf.nn.relu)
    #y3_out = add_layer(y2_out, 20, 10)
    #y4_out = add_layer(y3_out, 10 ,output_size)

    y_output_layer = y1_out
    prediction = tf.reshape(y_output_layer, shape=[-1, time_steps, output_size])


# Loss computing

    # cross_entropy =tf.multiply(tf.square(tf.subtract( tf.reshape(prediction, [-1]) ,  tf.reshape(ys, [-1]) )), 0.5)

    # loss_finial = tf.reduce_mean(cross_entropy)
    loss_final = tf.losses.mean_squared_error(ys,prediction)
    train = tf.train.GradientDescentOptimizer(LR).minimize(loss_final)
    #train = tf.train.AdamOptimizer(LR).minimize(loss_final)


    saver = tf.train.Saver()
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)

    for i in range(11):
        train_in, train_out, test_in, test_out = getbatch()
        train_result, loss = sess.run([train, loss_final], feed_dict={xs: train_in, ys: train_out})

        if i % 10 == 0:
            test_result, test_loss = sess.run([train, loss_final], feed_dict={xs: test_in, ys: test_out})
            print('train loss:', loss,'  test loss', test_loss)
            saver.save(sess, '/users/barry/desktop/LSTM_CODE/model.ckpt', global_step=i+1)

    path = '/users/barry/desktop/LSTM_CODE/model.ckpt'
    saver.save(sess, path)