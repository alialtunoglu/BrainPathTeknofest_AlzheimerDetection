<template>
  <nav class="bg-white shadow-md p-4">
    <div class="container mx-auto flex justify-between items-center">
      <NuxtLink to="/" class="flex text-4xl font-bold text-teal-600">
        BrainPath
        <Icon name="tabler:brain" size="50" class="text-teal-600" />
      </NuxtLink>

      <ul class="flex space-x-6">
        <li class="flex items-center">
          <NuxtLink to="/" class="hover:text-teal-200 text-teal-600">
            <Icon name="mdi:home" class="size-10" />
            <span class="hidden md:inline">Ana Sayfa</span>
          </NuxtLink>
        </li>
        <li class="flex items-center">
          <NuxtLink to="/about" class="hover:text-teal-200 text-teal-600">
            <Icon name="mdi:information" />
            <span class="hidden md:inline">Hakkımızda</span>
          </NuxtLink>
        </li>
        <li class="flex items-center">
          <NuxtLink to="/model" class="hover:text-teal-200 text-teal-600">
            <Icon name="mdi:brain" />
            <span class="hidden md:inline">Model</span>
          </NuxtLink>
        </li>
        <li class="flex items-center">
          <NuxtLink to="/team" class="hover:text-teal-200 text-teal-600">
            <Icon name="ic:sharp-groups" />
            <span class="hidden md:inline">Ekip</span>
          </NuxtLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup lang="ts">
// Navigasyon bileşeni
</script>

<style scoped></style>
