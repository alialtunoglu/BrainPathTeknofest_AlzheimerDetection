<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />
    <div class="container mx-auto py-8 px-4">
      <div class="bg-white p-6 rounded-lg shadow-md mb-7">
        <h1 class="text-4xl font-bold text-teal-600 mb-6">Biz Kimiz</h1>
        <p class="text-gray-700 mb-1">
          BrainPath takımı, 2024 yılında yazılım mühendisliği öğrencileri
          tarafından kurulmuştur. Ekip, yapay zeka alanında uzmanlaşmış
          öğrenciler ile frontend geliştirme konusunda yetenekli bireylerden
          oluşmaktadır. Takım, teknolojik yenilikler ve yapay zeka çözümleri
          üzerine odaklanarak, geleceğin dijital dünyasına katkıda bulunmayı
          hedeflemektedir.
        </p>
      </div>

      <h1 class="text-4xl font-bold text-teal-600 mb-6">Ekibimiz</h1>

      <div
        class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 text-black"
      >
        <!-- Ekip Üyesi 1 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4">
            <img src="../public/resimler/ali.png" alt="ali" />
          </div>
          <h2 class="text-xl font-bold text-center">Ali Altunoğlu</h2>
          <p class="text-center text-gray-600 mb-2">Proje Lideri</p>
          <p class="text-gray-700 text-center">
            MlOps, Computer Vision ve Back-End geliştirme. alialtunoglu02@gmail.com
          </p>
        </div>

        <!-- Ekip Üyesi 2 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4">
            <img src="../public/resimler/tarik.png" alt="tarık" />
          </div>
          <h2 class="text-xl font-bold text-center">Tarık Kılıç Alsancak</h2>
          <p class="text-center text-gray-600 mb-2">Frontend Developer</p>
          <p class="text-gray-700 text-center">
            Frontend geliştirme, Web uygulaması ve arayüz geliştirme
          </p>
        </div>

        <!-- Ekip Üyesi 3 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4">
            <img src="../public/resimler/sena.png" alt="senanur" />
          </div>
          <h2 class="text-xl font-bold text-center">Senanur Bayram</h2>
          <p class="text-center text-gray-600 mb-2">Proje Yöneticisi</p>
          <p class="text-gray-700 text-center">
            Literatür taraması, veri seti araştırması, model eğitimi ve optimi-
            zasyonu
          </p>
        </div>

        <!-- Ekip Üyesi 4 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <div class="w-24 h-24 bg-gray-200 rounded-full mx-auto mb-4">
            <img src="../public/resimler/murat.png" alt="murat" />
          </div>
          <h2 class="text-xl font-bold text-center">Murat Oğurlu</h2>
          <p class="text-center text-gray-600 mb-2">ML Developer</p>
          <p class="text-gray-700 text-center">
            Modelin geliştirilmesi, doğruluk testlerinin yapılması, optimizasyon
            süreçlerinin yürütülmesi
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
