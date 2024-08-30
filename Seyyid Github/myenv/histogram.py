import matplotlib.pyplot as plt
import numpy as np

# Rastgele veri
veri = np.random.randn(1000)

# Histogram oluşturma
plt.hist(veri, bins=30)

# Başlık ve etiketler ekleme
plt.title("dneme")
plt.xlabel("Değerler")
plt.ylabel("Frekans")

# Grafik gösterme
plt.show()
