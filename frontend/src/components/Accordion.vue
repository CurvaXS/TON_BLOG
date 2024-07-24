<template>
    <div class="accordion">
        <div class="row">
            <div class="col">
                <div class="tabs">
                    <div class="tab">
                        <input type="checkbox" id="chck1">
                        <label class="tab-label" for="chck1">Item 1</label>
                        <div class="tab-content">
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsum, reiciendis!
                        </div>
                    </div>
                    <div class="tab">
                        <input type="checkbox" id="chck2">
                        <label class="tab-label" for="chck2">Item 2</label>
                        <div class="tab-content">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. A, in!
                        </div>
                    </div>
                    <div class="tab">
                        <input type="checkbox" id="chck3">
                        <label class="tab-label" for="chck3">Item 3</label>
                        <div class="tab-content">
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsum, reiciendis!
                        </div>
                    </div>
                    <div class="tab">
                        <input type="checkbox" id="chck4">
                        <label class="tab-label" for="chck4">Item 4</label>
                        <div class="tab-content">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. A, in!
                        </div>
                    </div>
                    <div class="tab">
                        <input type="checkbox" id="chck5">
                        <label class="tab-label" for="chck5">Item 5</label>
                        <div class="tab-content">
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsum, reiciendis!
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script setup>
</script>

<style lang="scss">
$midnight: rgba(0, 0, 0, 0.45);
$clouds: rgb(236, 240, 241);

input {
    position: absolute;
    opacity: 0;
    z-index: -1;
}

.row {
    display: flex;

    .col {
        flex: 1;

        &:last-child {
            margin-left: 1em;
        }
    }
}

/* Accordion styles */
.tabs {
    overflow: hidden;
    // box-shadow: 0 4px 4px -2px rgba(0, 0, 0, 0.5);

    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    min-height: 77vh;
    padding-bottom: 60px;
}

.tab {
    width: 100%;
    color: white;
    overflow: hidden;
    background: rgb(188, 62, 108);
    background: linear-gradient(90deg, rgb(188, 62, 108) 0%, rgb(120, 16, 54) 50%, rgb(188, 62, 108) 100%);
    border-radius: 10px;
    padding: 1.5px 2px;
    margin-bottom: 16px;

    &-label {
        display: flex;
        justify-content: space-between;

        background: rgb(0, 0, 0);
        padding: 1.1em;
        border-radius: 10px;

        font-family: Roboto;
        font-size: 18px;
        font-weight: 700;
        line-height: 150%;

        cursor: pointer;

        /* Icon */
        &:hover {
            background: rgba(0, 0, 0, 0.8);
        }

        &::after {
            content: "+";
            width: 1.5em;
            // height: 1.5em;
            text-align: center;
            transition: all .35s;
            font-size: 30px;
            font-weight: 100;
        }
    }

    &-content {
        max-height: 0;
        padding: 0 1em;
        color: #FFF;
        background: #000;
        transition: all .35s;
        // border-radius: 10px;
        border-end-end-radius: 10px;
        border-end-start-radius: 10px;
    }

    &-close {
        display: flex;
        justify-content: flex-end;
        padding: 1em;
        font-size: 0.75em;
        background: $midnight;
        cursor: pointer;
        transition: all .35s;

        &:hover {
            background: darken($midnight, 10%);
        }
    }
}

// :checked
input:checked {
    +.tab-label {
        transition: all .35s;
        background: darken($midnight, 10%);
        border-end-end-radius: 0px;
        border-end-start-radius: 0px;

        &::after {
            transform: rotate(45deg);
        }
    }

    ~.tab-content {
        max-height: 100vh;
        padding: 1em;
    }
}
</style>