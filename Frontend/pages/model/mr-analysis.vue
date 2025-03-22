<script setup lang="ts"></script>

<template>
  <div class="min-h-screen bg-gray-50">
    <NavBar />

    <div class="container mx-auto py-8 px-4">
      <h1 class="text-4xl font-bold text-teal-600 mb-6">Model</h1>

      <UploadForm type="goruntu" />
      <UButton
        class="my-10 bg-teal-500 hover:bg-teal-400"
        size="xl"
        variant="outline"
        icon="ant-design-radius-setting-outlined"
        color="neutral"
        disabled
      >
        Analiz et
      </UButton>
    </div>
  </div>
</template>
