<template>
  <div>
    <h1>Welcome!</h1>
    <p>Your email is: {{ email }}</p>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();

// Use a computed property to reactively access the email query parameter
const email = computed(() => route.query?.email || 'unkown email');
</script>

<style scoped>
/* Add any styles for your welcome message component here */
h1 {
  color: #333;
}

p {
  color: #666;
}
</style>
