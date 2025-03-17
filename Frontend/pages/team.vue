<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />
    <div class="container mx-auto py-8 px-4">
      <h1 class="text-4xl font-bold text-teal-600 mb-6">Ekibimiz</h1>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Ekip Üyesi 1 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div>
          <h2 class="text-xl font-bold text-center">Ahmet Yılmaz</h2>
          <p class="text-center text-gray-600 mb-2">Proje Lideri</p>
          <p class="text-gray-700 text-center">
            Yapay zeka ve görüntü işleme alanında 5 yıllık deneyim
          </p>
        </div>

        <!-- Ekip Üyesi 2 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div>
          <h2 class="text-xl font-bold text-center">Ayşe Demir</h2>
          <p class="text-center text-gray-600 mb-2">Veri Bilimci</p>
          <p class="text-gray-700 text-center">
            Derin öğrenme modellerinin geliştirilmesi ve iyileştirilmesi
          </p>
        </div>

        <!-- Ekip Üyesi 3 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4"></div>
          <h2 class="text-xl font-bold text-center">Mehmet Kaya</h2>
          <p class="text-center text-gray-600 mb-2">Yazılım Geliştirici</p>
          <p class="text-gray-700 text-center">
            Web uygulaması ve arayüz geliştirme uzmanı
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Ekip sayfası için hazırlanan komponent
</script>

<style scoped>
/* Sayfa stillemesi buraya gelecek */
</style>
