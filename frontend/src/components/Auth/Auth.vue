<script setup>
import Navbar from './Navbar.vue';
import Aside from './Aside.vue';
import { RouterView } from 'vue-router';
import { ref, onMounted } from 'vue';
import ClipLoader from 'vue-spinner/src/ClipLoader.vue'
import axios from 'axios'
import { useRoute, RouterLink, useRouter } from 'vue-router';

const route = useRoute();

const emit = defineEmits(['logout'])

const me = ref(null)
const meImage = ref(null)
const loadingProfile = ref(true)

const color = ref('red')
const size = ref('100px')


const props = defineProps({
  access_token: String
})

onMounted(async () => {
  try {
    if (props.access_token) {
      // Decode the JWT token
      const base64Url = props.access_token.split('.')[1] // Get the payload part of the token
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split('')
          .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
          .join('')
      )

      const payload = JSON.parse(jsonPayload) // Parse the payload

      const user_id = payload.user_id // Assuming 'user_id' exists in the payload

      const response = await axios.get(`/api/users/user_id/${user_id}`)
      me.value = response.data

      try {
        const response = await axios.get(`/api/users/upload/${user_id}`, { responseType: 'blob' })
        const blobUrl = URL.createObjectURL(response.data);
        meImage.value = blobUrl
        loadingProfile.value = false
      } catch (error) {
        console.log(error)
      }
    } else {
      console.log('No access token provided.')
    }
  } catch (error) {
    console.error('Error decoding access token:', error)
  }
})
</script>


<template>
  <ClipLoader v-if="loadingProfile" :color="color" :size="size" class="flex items-center justify-center h-screen" />
  <Navbar v-if="!loadingProfile" />
  <Aside v-if="!loadingProfile" @logout="emit('logout')" :me="me" :meImage="meImage" />
  <RouterView :key="`${$route.params.id}-${$route.params.username}`" />
</template>