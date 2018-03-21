<template>
    <div id="app" class="container">

        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
        </div>
        <p>곧 새사 기사 상자를 마련해야겠군요!</p>
        <div class="row">
            <input v-model="title" placeholder="제목을 입력해주세요">
        </div>
        <div class="row">
            <input v-model="link" placeholder="링크를 입력해주세요">
        </div>
        <div class="row">
            <button type="button" class="btn btn-success">
                정리해보고 싶은 기사인가요?
            </button>
        </div>
        <div class="row">
            #자기계발 
            +태그추가 
        </div>
        <div>
            <p>다시 읽고 싶은 만큼 점수를 매겨주세요!</p>
        </div>
        <div class="row">
            <button type="button" class="btn btn-success">
                업로드!
            </button>
        </div>

    </div>
</template>

<script>
  export default {


  }

</script>
