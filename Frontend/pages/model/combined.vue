<script setup lang="ts"></script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />

    <div class="flex flex-col mx-45">
      <h1 class="text-4xl font-bold text-teal-600 mt-8 ml-5">Model</h1>
      <div class="flex flex-row gap-4">
        <div class="container mx-auto py-8 px-4">
          <div class="bg-white p-6 rounded-lg shadow-md mb-8">
            <h2 class="text-2xl font-bold text-teal-600 mb-4">
              MR Görüntü Analizi
            </h2>
            <UploadForm />
          </div>
        </div>

        <div class="container mx-auto py-8 px-4">
          <div class="bg-white p-6 rounded-lg shadow-md mb-8">
            <h2 class="text-2xl font-bold text-teal-600 mb-4">
              MR Görüntü Analizi
            </h2>
            <UploadForm />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
