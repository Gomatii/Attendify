import tensorflow as tf

def main():
    result = tf.reduce_sum(tf.random.normal([1000, 1000]))
    print(result)

if __name__ == "__main__":
    main()

