<script setup lang="ts">
defineProps<{
  title: string
  url: string
}>()
</script>

<template>
  <a class="button" :href="url">{{ title }}</a>
</template>
