<script setup lang="ts">
const route = useRoute();

useHead({
  meta: [{ property: "og:title", content: `BrainPath - ${route.meta.title}` }],
});
</script>

<template>
  <div>
    <Navbar />

    <main>
      <Nuxt />
    </main>

    <footer>
      <p>Teknofest yarışması için düzenlenen proje</p>
      <p>&copy; 2023 Şirket Adı. Tüm hakları saklıdır.</p>
    </footer>
  </div>
</template>
