import { createApp } from "vue";
import naive from "naive-ui";
import App from "./App.vue";
import "vfonts/Lato.css";
// Monospace Font
import "vfonts/FiraCode.css";
// then it works
const app = createApp(App);
app.use(naive);
app.mount("#app");
