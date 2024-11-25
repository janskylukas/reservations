<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const confirmPassword = ref('')
</script>

<template>
  <main>
    <header>
      <h1>Welcome to ✨The Reservations✨</h1>

      <h2>Register</h2>
      <p>To proceed to The Reservations, please register.</p>
    </header>

    <form @submit.prevent="">
      <label>
        E-mail:
        <input type="email" v-model="email" placeholder="Enter e-mail" />
      </label>
      <label>
        Password:
        <input type="password" v-model="password" placeholder="Enter password" />
      </label>
      <label>
        Confirm Password:
        <input type="password" v-model="confirmPassword" placeholder="Confirm password" />
      </label>

      <input type="submit" value="Login" />
    </form>
    <footer>
      <p>Do you already have an account? <RouterLink to="/login">Login</RouterLink></p>
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
