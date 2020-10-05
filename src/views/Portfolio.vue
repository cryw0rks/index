<template>
    <div class="cry-portfolio cry-box">
        <h1 class="cry-box-title">portfolio - sometimes we are bad lol</h1>
        <div class="cry-work-main">
            <div v-for="row in dataPortfolio" :key="row.id" class="cry-work-list">
                <a :href="row.website" target="_blank">
                    <div class="cry-work-content" :style="{'background': 'url('+row.background +')', 'background-size': 'cover', 'background-repeat': 'no-repeat', 'background-position': 'center top'}">
                        <div class="cry-work-content-inside">
                            <div class="cry-work-content-name">
                                <span><b>{{ row.name }}</b> - {{ row.service }}</span>
                            </div>
                            <div class="cry-work-content-website">
                                <a :href="row.website" target="_blank">{{ row.website }}</a>
                            </div>
                            <div class="cry-work-content-description">
                                <p>{{ row.description }}</p>
                            </div>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dataPortfolio: null,
    };
  },
  methods: {
    async getData() {
      const data = await axios.get(`https://raw.githubusercontent.com/cryw0rks/website/master/public/data/portfolio.json`);
      this.dataPortfolio = data.data;
    },
  },
  mounted() {
    this.getData();
  },
};
</script>