<template>
  <div>
    <!-- Navbar Bileşeni -->
    <Navbar />

    <!-- Sayfa İçeriği -->
    <main>
      <Nuxt />
    </main>

    <!-- Altbilgi -->
    <footer>
      <p>&copy; 2023 Şirket Adı. Tüm hakları saklıdır.</p>
    </footer>
  </div>
</template>

<script>
import Navbar from "~/components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>

<style scoped>
/* Basit stil örnekleri */
main {
  padding: 20px;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #f8f8f8;
  border-top: 1px solid #e7e7e7;
}
</style>
