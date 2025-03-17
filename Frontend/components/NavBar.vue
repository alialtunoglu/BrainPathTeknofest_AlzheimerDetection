<template>
  <nav class="bg-white shadow-md p-4">
    <div class="container mx-auto flex justify-between items-center">
      <div class="text-xl font-bold text-teal-600">BrainPath</div>
      <ul class="flex space-x-6">
        <li>
          <NuxtLink to="/" class="hover:text-teal-200 text-teal-600"
            >Ana Sayfa</NuxtLink
          >
        </li>
        <li>
          <NuxtLink to="/about" class="hover:text-teal-200 text-teal-600"
            >Hakkımızda</NuxtLink
          >
        </li>
        <li>
          <NuxtLink to="/model" class="hover:text-teal-200 text-teal-600"
            >Model</NuxtLink
          >
        </li>
        <li>
          <NuxtLink to="/team" class="hover:text-teal-200 text-teal-600"
            >Ekip</NuxtLink
          >
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup lang="ts">
// Navigasyon bileşeni
</script>

<style scoped>
/* Navigasyon stillemesi */
</style>
