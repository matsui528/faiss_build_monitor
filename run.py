import faiss
print("===== faiss version =====")
print(faiss.__version__)

import numpy
print("===== numpy config =====")
numpy.__config__.show()


print("===== Run simple kmeans =====")
err = faiss.Kmeans(10, 20).train(numpy.random.rand(1000, 10).astype('float32'))
print(err)
