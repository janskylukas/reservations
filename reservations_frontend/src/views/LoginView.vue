<script setup lang="ts">
import { login } from '@/services/authService';
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const error = ref('');
const username = ref('');
const password = ref('');

const Login = async () => {
  if (!username.value || !password.value) {
    return error.value = 'Please enter username and password';
  }

  try {
    const response = await login({ username: username.value, password: password.value });
    await router.push('/')
  } catch (e) {
    return error.value = 'Invalid username or password';
  }


}
</script>

<template>
  <main>
    <header>
      <h1>Welcome to ✨The Reservations✨</h1>

      <h2>Login</h2>
      <p>To proceed to The Reservations, please login.</p>
    </header>

    <form @submit.prevent="Login">
      <label>
        Username:
        <input type="username" v-model="username" placeholder="Enter username" />
      </label>
      <label>
        Password:
        <input type="password" v-model="password" placeholder="Enter password" />
      </label>

      <input type="submit" value="Login" />
    </form>
    <p v-if="error">{{ error }}</p>
    <footer>
      <p>Don't have an account? <RouterLink to="/register">Register</RouterLink>
      </p>
    </footer>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
  height: 100vh;
}

header {
  padding: 1.5rem;
}

footer {
  padding: 1.5rem;
  width: 100%;
  text-align: center;
  padding-bottom: 3rem;
}

form {
  flex: 1 1 0%;
}

h2 {
  padding: 1.5rem;
}
</style>
