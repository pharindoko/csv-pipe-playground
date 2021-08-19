<template>
  <n-config-provider :theme="darkTheme">
    <FileUploadTest></FileUploadTest>
  </n-config-provider>
</template>

<script setup>
import FileUploadTest from './components/FileUploadTest.vue';
import { darkTheme } from 'naive-ui';




</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
  color: rgba(255, 255, 255, 0.82);
}
</style>



