# coding=utf-8
import tensorflow as tf

with tf.compat.v1.Session() as sess:
    #搭建网络
    x=tf.compat.v1.placeholder(tf.float32,name='x')
    y=tf.compat.v1.placeholder(tf.float32,name='y')
    b=tf.Variable(1.,name='b')
    xy=tf.multiply(x,y)
    op=tf.add(xy,b,name='op')
    sess.run(tf.compat.v1.global_variables_initializer())
    print('----------------------')
    print(sess.run(op,feed_dict={x:2,y:3}))

    # #ckpt保存
    # saver=tf.compat.v1.train.Saver()
    # saver.save(sess,'ckpt/model_ck')

    #pb保存
    constant_graph=tf.graph_util.convert_variables_to_constants(sess,sess.graph_def,['op'])
    with tf.gfile.FastGFile('pb/model.pb','wb') as f:
        f.write(constant_graph.SerializeToString())

    # #savedmodel文件保存
    # builder=tf.compat.v1.saved_model.builder.SavedModelBuilder('savemodel')
    # builder.add_meta_graph_and_variables(sess,['cpu_server_1'])
    # builder.save()

    print('----------------------')
    print('over')


    # #ckpt加载
    # saver=tf.compat.v1.train.import_meta_graph('ckpt/model_ck.meta')
    # saver.restore(sess,tf.train.latest_checkpoint('ckpt'))

    #pb加载
    with tf.gfile.FastGFile('pb/model.pb','rb') as f:
        graph_def=tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def,name='')

    # #savemodel加载
    # tf.saved_model.loader.load(sess, ['cpu_server_1'], 'savemodel')

    #测试模型加载是否成功
    input_x = sess.graph.get_tensor_by_name('x:0')
    input_y = sess.graph.get_tensor_by_name('y:0')
    op = sess.graph.get_tensor_by_name('op:0')
    ret = sess.run(op, feed_dict={input_x: 5, input_y: 5})
    print('----------------------')
    print(ret)