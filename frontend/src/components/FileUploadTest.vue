<template>
    <n-h1>
        <n-text type="primary">pipe playground</n-text>
    </n-h1>

    <n-grid :x-gap="12" :cols="3">
        <n-grid-item :offset="1">
            <n-card id="fs-upload-files" style="text-align:center">
                <FileUpload
                    ref="upload"
                    post-action="http://127.0.0.1:8000/uploadfile/"
                    :multiple="true"
                    drop=".droparea"
                    :drop-directory="true"
                    v-model="files"
                    @input-filter="inputFilter"
                >
                    <n-button type="primary">Select file</n-button>
                </FileUpload>
                <n-divider dashed>or</n-divider>

                <div class="droparea" align-text="center">
                    <n-space vertical>
                        <h3>
                            <n-text>
                                drop your files
                                <br />
                                <n-text type="info">(allowed format: csv)</n-text>
                            </n-text>
                        </h3>
                    </n-space>
                    <ul>
                        <li v-for="file of files" :key="file.id">{{ file.id }} - {{ file.name }}</li>
                    </ul>
                </div>

                <br />
                <n-divider>
                    <n-button
                        type="primary"
                        @click.prevent="upload.active = true"
                        :disabled="files.length == 0 && (upload != null && upload.active == false)"
                    >Upload</n-button>
                </n-divider>
            </n-card>
        </n-grid-item>
    </n-grid>
</template>

<style>
.exampl .example-drag label.btn {
    margin-bottom: 0;
    margin-right: 1rem;
}
.droparea {
    border: 3px dashed lightblue;
    min-height: 300px;
}
.example-drag .drop-active {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    position: fixed;
    z-index: 9999;
    opacity: 0.6;
    text-align: center;
    background: #000;
}
.example-drag .drop-active h3 {
    margin: -0.5em 0 0;
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    -webkit-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    font-size: 40px;
    color: #fff;
    padding: 0;
}
</style>
<script lang="ts">
import { SetupContext, ref, Ref, defineComponent, watch } from "vue"
import FileUpload, { VueUploadItem } from 'vue-upload-component'

export default defineComponent({
    components: {
        FileUpload,
    },
    setup(props: any, context: SetupContext) {
        const upload = ref<any>(null)
        let files: Ref<VueUploadItem[]> = ref([])
        watch(upload, function (newUpload: any) {
            console.log("file", newUpload.files)
        })
        return {
            upload,
            files,
        }
    },
    methods: {
        inputFilter(newFile, oldFile, prevent) {
            console.log('ff')
            if (newFile && !oldFile && newFile.name.search(/\.(csv)$/i) === -1) {
                return prevent()
            }
        }
    }
})
</script>