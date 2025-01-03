<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import axios from 'axios';


const popUser = ref(null)
const popImage = ref(null)

const emit = defineEmits(['lastPinLoaded'])

const user = ref(null);
const pinImage = ref(null);
const pinVideo = ref(null)
const imageLoaded = ref(false); // Флаг загрузки изображения
const videoLoaded = ref(false); // Флаг загрузки видео

const userImage = ref(null);

const showPopover = ref(false); // State to control the popover visibility

const insidePopover = ref(false)

const bgSave = ref('bg-red-700')
const saveText = ref('Save')

const props = defineProps({
  pin: Object,
  lastPinId: Number,
  showAllPins: Boolean
});

const onImageLoad = () => {
  imageLoaded.value = true;
};

const onVideoLoad = () => {
  videoLoaded.value = true;
}

const showSaveButton = ref(false)

onMounted(async () => {
  try {
    const response = await axios.get(`/api/users/user_id/${props.pin.user_id}`);
    user.value = response.data;

    try {
      const userResponse = await axios.get(`/api/users/upload/${user.value.id}`, { responseType: 'blob' });
      const blobUrl = URL.createObjectURL(userResponse.data);
      userImage.value = blobUrl;
    } catch (error) {
      console.error(error);
    }

    try {
      const pinResponse = await axios.get(`/api/pins/upload/${props.pin.id}`, { responseType: 'blob' });
      const blobUrl = URL.createObjectURL(pinResponse.data);
      const contentType = pinResponse.headers['content-type'];
      if (contentType.startsWith('image/')) {
        pinImage.value = blobUrl;
      } else {
        pinVideo.value = blobUrl;
      }
      if (props.pin.id === props.lastPinId) {
        emit('lastPinLoaded');
      }
    } catch (error) {
      console.error(error);
    }
  } catch (error) {
    console.error(error);
  }
});

async function loadUser() {
  try {
    const response = await axios.get(`/api/users/user_id/${props.pin.user_id}`)
    popUser.value = response.data
    try {
      const response = await axios.get(`/api/users/upload/${props.pin.user_id}`, { responseType: 'blob' })
      const blobUrl = URL.createObjectURL(response.data);
      popImage.value = blobUrl
    } catch (error) {
      console.error(error)
    }
  } catch (error) {
    console.error(error)
  }
}

async function save() {
  bgSave.value = 'bg-black'
  saveText.value = 'Saving...'
  try {
    const response = await axios.post(`/api/pins/user_saved_pins/${props.pin.id}`, {
      withCredentials: true
    })
    saveText.value = 'Saved'

  } catch (error) {
    if (error.response.status === 409) {
      saveText.value = 'U already saved!'
    }
  }
}
</script>

<template>
  <div class="w-1/5 p-2">
    <div class="relative block hover:opacity-90" @mouseover="showSaveButton = true"
      @mouseleave="showSaveButton = false">
      <button v-if="showSaveButton" @click.stop="save"
        :class="`absolute z-50 top-2 right-2 px-6 py-3 text-sm ${bgSave} text-white rounded-3xl transition`">
        {{ saveText }}
      </button>
      <RouterLink :to="`/pin/${pin.id}`">
        <div v-show="!showAllPins" :class="['w-full', 'rounded-3xl']"
          :style="{ backgroundColor: pin.rgb, height: pin.height + 'px' }">
        </div>
        <div v-show="showAllPins">
          <img v-if="pinImage" :src="pinImage" @load="onImageLoad" alt="pin image" class="w-full h-auto rounded-3xl" />
          <video v-if="pinVideo" :src="pinVideo" @loadeddata="onVideoLoad" class="w-full h-auto rounded-3xl" autoplay
            loop muted />
        </div>
        <p v-if="pin.title" class="mt-2 text-sm"> {{ pin.title }}</p>
      </RouterLink>
    </div>

    <RouterLink v-if="user" :to="`/user/${user.username}`" @mouseover="showPopover = true; loadUser()"
      @mouseleave="if (!insidePopover) showPopover = false;"
      class="flex items-center mt-2 hover:underline cursor-pointer relative">
      <div v-if="!showAllPins" class="bg-gray-300 w-8 h-8 rounded-full"></div>
      <img v-else :src="userImage" alt="user profile" class="w-8 h-8 rounded-full object-cover" />
      <span v-if="user" class="ml-2 text-sm font-medium"> {{ user.username }}</span>

      <div v-show="showPopover" @mouseover="insidePopover = true"
        @mouseleave="insidePopover = false; showPopover = false"
        class="absolute top-[30px] left-[5px] bg-white shadow-2xl rounded-xl px-4 py-2 text-sm font-medium text-gray-700 z-30 h-32 w-32">
        <div class="flex flex-col items-center justify-center">
          <img v-if="popImage" :src="popImage" class="mb-2 rounded-full w-16 h-16 object-cover" />
          <div v-else class="bg-red-300 mb-2 rounded-full w-16 h-16"></div>
          <RouterLink v-if="popUser" :to="`/user/${popUser.username}`"
            class="text-center text-sm font-medium hover:underline">@{{ popUser.username }}</RouterLink>
        </div>
      </div>
    </RouterLink>

    <div v-else class="flex items-center mt-2 hover:underline cursor-pointer">
      <div class="bg-gray-300 w-8 h-8 rounded-full"></div>
      <span class="ml-2 text-sm font-medium"></span>
    </div>
  </div>
</template>