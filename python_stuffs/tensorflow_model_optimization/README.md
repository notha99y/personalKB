# Useful links
- https://www.tensorflow.org/lite/performance/model_optimization
- https://www.tensorflow.org/model_optimization
- https://github.com/tensorflow/model-optimization
- https://blog.tensorflow.org/2018/09/introducing-model-optimization-toolkit.html

# Types of Optimization
- Quantization
- Pruning
- Clustering

## Quantization
- [Integer Quantization Blog](https://blog.tensorflow.org/2019/06/tensorflow-integer-quantization.html)
- [Quantization Aware Training Blog](https://blog.tensorflow.org/2020/04/quantization-aware-training-with-tensorflow-model-optimization-toolkit.html)

Quantiztion works by reducing the precision of the numbers used to represent a model's paramters, which by default are 32-bit floating point numbers. This results in a smaller model size and faster computation

- [Post-training float16 quantization](https://www.tensorflow.org/lite/performance/post_training_float16_quant)
- [Post-training dynamic range quanitzation](https://www.tensorflow.org/lite/performance/post_training_quant)
- [Post-training integer quantization](https://www.tensorflow.org/lite/performance/post_training_integer_quant)
- [Quantization-aware training](http://www.tensorflow.org/model_optimization/guide/quantization/training)
- [Quantization with int16 activations](https://www.tensorflow.org/model_optimization/guide/quantization/post_training)

## Pruning
- [blog](https://blog.tensorflow.org/2019/05/tf-model-optimization-toolkit-pruning-API.html)

[Pruning](https://www.tensorflow.org/model_optimization/guide/pruning) works by removing parameters within a model that have only a minor impact on its predictions. Pruned models are the same size on disk and have the same runtime latency, but can be compressed more effectively. This makes pruning a useful technique for reducing model download size.


## Clustering
- [blog](https://blog.tensorflow.org/2020/08/tensorflow-model-optimization-toolkit-weight-clustering-api.html) 

[Clustering](https://www.tensorflow.org/model_optimization/guide/clustering) works by grouping weights of each layer in a model into a predefined numbers of clusters, then sharing the centroid values for the weights belonging to each individual cluster. This reduces the number of unique weight values in a model, thus reudcing its complexity. As a result, clustered models can be compressed more effectively, providing deployment benefits similar to pruning

# Hardwares
- CPU
- GPU (Android)
- Edge TPU
- Hexagon DSP