<template>
    <div>
        


        <b-card class="result">
            <b-tabs pills card vertical>
                <b-tab title="Top1" active>
                    <b-card-text>
                        <div>
                            <h1>브랜드이름</h1>
                            <b-tabs content-class="mt-3">
                                <b-tab title="브랜드 정보" active>
                                    <div>
                                        <b-table striped hover :items="items"></b-table>
                                    </div>
                                </b-tab>
                                <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                            </b-tabs>
                        </div>
                    </b-card-text></b-tab>
                <b-tab title="Top2"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top3"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top4"><b-card-text>
                      <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top5"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top6"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top7"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top8"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top9"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
                <b-tab title="Top10"><b-card-text>
                    <div>
                        <h1>"A 브랜드"</h1>
                        <b-tabs content-class="mt-3">
                            <b-tab title="브랜드 정보" active><p>브랜드 상세정보</p></b-tab>
                            <b-tab title="본사 정보"><p>본사 정보</p></b-tab>
                        </b-tabs>
                    </div>
                    </b-card-text></b-tab>
            </b-tabs>
        </b-card>
    </div>

</template>
<script>
export default {
    data() {
        return {
            items: [
                { franchise_months: '10',startup_cost: '200000',average_sales: '3500000',open_rate: '15',close_rate: '20'}
            ]
        }
    }
    
}
</script>

<style>
.result{
    margin-top: 0px;
    height: 900px;
}
</style>