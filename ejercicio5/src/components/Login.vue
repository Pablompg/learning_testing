<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="submitLogin">
      <div class="form-group">
        <label for="email">Email:</label>
        <input
          type="email"
          id="email"
          v-model="loginForm.email"
          required
          placeholder="Enter your email"
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input
          type="password"
          id="password"
          v-model="loginForm.password"
          required
          placeholder="Enter your password"
        />
      </div>
      <button type="submit" :disabled="!isFormValid">Login</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const loginForm = ref({
  email: '',
  password: '',
});

const isFormValid = computed(() => {
  return loginForm.value.email && loginForm.value.password;
});

function submitLogin() {
  if (isFormValid.value) {
    router.push({ path: '/welcome', query: { email: loginForm.value.email } });
  }
}
</script>

<style scoped>
input {
  margin-bottom: 0.5rem;
}

</style>
