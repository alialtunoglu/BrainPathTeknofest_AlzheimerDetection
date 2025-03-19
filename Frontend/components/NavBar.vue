<script setup lang="ts">
const items = [
  {
    label: "Home",
    icon: "mdi:home",
    to: "/",
    class: "text-xl",
  },
  {
    label: "Hakkımızda",
    icon: "mdi:information",
    to: "/about",
    class: "text-xl",
  },
  {
    label: "Modeller",
    icon: "mdi:brain",
    slot: "models",
    class: "text-xl",
    children: [
      {
        label: "MR",
        description: "MR Görüntü Analizi",
        to: "/model/mr-analysis",
      },
      {
        label: "El yazı",
        description: "El yazısı tanıma",
        to: "/model/handwriting",
      },
      {
        label: "MR + El yazı",
        description: "MR + El yazı birleşimi",
        to: "/model/combined",
      },
    ],
  },
  {
    label: "Ekip",
    icon: "ic:sharp-groups",
    to: "/team",
    class: "text-xl",
  },
];
</script>

<template>
  <nav class="bg-white shadow-md p-4">
    <div class="container mx-auto flex justify-between items-center">
      <NuxtLink to="/" class="flex text-4xl font-bold text-teal-600">
        BrainPath
        <Icon name="tabler:brain" size="50" class="text-teal-600" />
      </NuxtLink>

      <UNavigationMenu
        :items="items"
        color="neutral"
        class="flex"
        :ui="{
          list: 'gap-4',
          item: '',
          viewport: 'mt-2 -mr-20 w-60',
          content: 'bg-white rounded-lg shadow-md w-full',
          childList: 'flex w-20',
          childLinkDescription: 'text-balance line-clamp-2 text-sm',
        }"
      >
        <template #models-content="{ item }">
          <div class="flex p-3">
            <ul class="space-y-2 w-full">
              <li v-for="child in item.children" :key="child.label">
                <NuxtLink
                  :to="child.to"
                  class="block p-2 rounded-lg hover:bg-teal-100 transition-colors"
                >
                  <p class="font-medium text-xl text-gray-900">
                    {{ child.label }}
                  </p>
                  <p class="text-sm text-gray-600">
                    {{ child.description }}
                  </p>
                </NuxtLink>
              </li>
            </ul>
          </div>
        </template>
      </UNavigationMenu>
    </div>
  </nav>
</template>
