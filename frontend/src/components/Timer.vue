<template>
    <div class="flip-clock">
        <template v-for="data in timeData" :key="data.label">
            <span class="flip-clock__piece" :id="data.elementId" v-show="data.show">
                <div>
                    <span class="no-animation__card">{{ twoDigits(data.current) }}</span>
                </div>
                <span v-if="showLabels" class="flip-clock__slot" :style="labelSize ? `font-size:${labelSize}` : ''">{{
            data.label }}</span>
            </span>
        </template>
    </div>
</template>

<script>
import {
    computed,
    onBeforeMount,
    onMounted,
    onUnmounted,
    toRefs,
    ref,
    watch
} from 'vue'
import moment from "moment";
import { v4 as uuidv4 } from 'uuid';

const fmt = "YYYY-MM-DD HH:mm:ss";

export default {
    name: 'vue3-flip-countdown',
    emits: ["timeElapsed"],
    props: {
        deadline: {
            type: String,
            required: false,
            default: moment().add(7, "d").add(10, "s").format(fmt),
        },
        deadlineISO: {
            type: String,
            required: false,
        },
        deadlineDate: {
            type: Date,
            required: false,
        },
        countdownSize: {
            type: String,
            required: false,
        },
        labelSize: {
            type: String,
            required: false,
        },
        stop: {
            type: Boolean,
            required: false,
        },

        showDays: {
            type: Boolean,
            required: false,
            default: true,
        },
        showHours: {
            type: Boolean,
            required: false,
            default: true,
        },
        showMinutes: {
            type: Boolean,
            required: false,
            default: true,
        },
        showSeconds: {
            type: Boolean,
            required: false,
            default: true,
        },
        showLabels: {
            type: Boolean,
            required: false,
            default: true,
        },
        labels: {
            type: Object,
            required: false,
            default: () => ({
                days: 'D',
                hours: 'H',
                minutes: 'M',
                seconds: 'S',
            }),
        },
        mainColor: {
            type: String,
            default: '#7F35FF'
        },
        secondFlipColor: {
            type: String,
            default: (props) => props.mainColor,
        },

        labelColor: {
            type: String,
            default: '#7F35FF'
        }
    },
    setup(props, { emit }) {
        const {
            deadline,
            stop,
            showDays,
            showHours,
            showMinutes,
            showSeconds,
            labels,
            deadlineDate,
            deadlineISO
        } = toRefs(props);

        const uuid = uuidv4();
        const now = ref(Math.trunc(new Date().getTime() / 1000));
        const date = ref(null);
        const interval = ref(null);
        const diff = ref(0);
        const show = ref(false);
        const timeData = ref([
            { current: 0, previous: 0, label: labels.value.days, elementId: 'flip-card-days-' + uuid, show: showDays.value },
            { current: 0, previous: 0, label: labels.value.hours, elementId: 'flip-card-hours-' + uuid, show: showHours.value },
            { current: 0, previous: 0, label: labels.value.minutes, elementId: 'flip-card-minutes-' + uuid, show: showMinutes.value },
            { current: 0, previous: 0, label: labels.value.seconds, elementId: 'flip-card-seconds-' + uuid, show: showSeconds.value },
        ]);

        const updateAllCards = () => {
            updateTime(0, days);
            updateTime(1, hours);
            updateTime(2, minutes);
            updateTime(3, seconds);
        }

        const twoDigits = (value) => {
            if (value != undefined) {
                if (value.toString().length <= 1) {
                    return '0' + value.toString();
                }
                return value.toString();
            } else {
                return '00';
            }
        }

        const updateTime = (idx, newValue) => {
            if (idx >= timeData.value.length || newValue === undefined) {
                return;
            }

            const d = timeData.value[idx];
            const val = newValue.value < 0 ? 0 : newValue.value;
            const el = document.querySelector(`#${d.elementId}`);

            if (val !== d.current) {
                d.previous = d.current;
                d.current = val;

                if (el) {
                    el.classList.remove('flip');
                    void el.offsetWidth;
                    el.classList.add('flip');
                }
            }
        }

        watch(deadline, (newVal) => {
            const endTime = newVal;
            date.value = Math.trunc(Date.parse(endTime.replace(/-/g, '/')) / 1000);
            if (!date.value) {
                throw new Error("Invalid props value, correct the 'deadline'");
            }
        })

        watch(now, () => {
            diff.value = date.value - now.value;
            if (diff.value <= 0 || stop.value) {
                diff.value = 0;
                updateTime(3, 0);
            } else {
                updateAllCards();
            }
        })

        watch(diff, (newVal) => {
            if (newVal == 0) {
                emit('timeElapsed');
                updateAllCards();
            }
        })

        const seconds = computed(() => Math.trunc(diff.value) % 60);
        const minutes = computed(() => Math.trunc(diff.value / 60) % 60);
        const hours = computed(() => Math.trunc(diff.value / 60 / 60) % 24);
        const days = computed(() => Math.trunc(diff.value / 60 / 60 / 24));

        onMounted(() => {
            if (diff.value !== 0) {
                show.value = true;
            }
        });

        onBeforeMount(() => {
            if (!deadline.value) {
                throw new Error("Missing props 'deadline'");
            }
            const endTime = deadline.value;
            let epoch = Date.parse(endTime.replace(/-/g, '/'));
            if (deadlineDate.value != null) {
                epoch = Date.parse(deadlineDate.value)
            }
            if (deadlineISO.value) {
                epoch = Date.parse(deadlineISO.value);
            }
            date.value = Math.trunc(epoch / 1000);
            if (!date.value) {
                throw new Error("Invalid props value, correct the 'deadline'");
            }
            interval.value = setInterval(() => {
                now.value = Math.trunc(new Date().getTime() / 1000);
            }, 1000);

        });

        onUnmounted(() => {
            clearInterval(interval.value);
        });

        return {
            now,
            date,
            interval,
            diff,
            show,
            timeData,
            twoDigits,
            emit,
        }
    }
};
</script>

<style scoped lang="scss">
.no-animation__card {
    color: rgb(127, 53, 255);
    font-size: 80px;
    font-weight: 700;
    line-height: 96px;
    display: block;
    color: v-bind(mainColor);
}

.flip-clock {
    text-align: center;
    perspective: 600px;
    margin: 0 auto;

    display: flex;
    justify-content: center;
    align-items: center;



    span {
        display: flex;
        justify-content: flex-start;
        align-items: center;

        margin-right: 10px;
    }

    *,
    *:before,
    *:after {
        box-sizing: border-box;
    }
}

.flip-clock__piece {
    display: inline-block;
    margin: 0 0.2vw;

    @media (min-width: 1000px) {
        margin: 0;
    }
}

.flip-clock__slot {
    color: rgb(127, 53, 255);
    font-size: 70px;
    font-weight: 700;
    line-height: 96px;
    display: block;
    color: v-bind(labelColor);
}

@media (max-width: 1100px) {
    .no-animation__card {
        font-size: 70px;
    }

    .flip-clock__slot {
        font-size: 65px;
    }
}

@media (max-width: 950px) {
    .no-animation__card {
        font-size: 30px;
    }

    .flip-clock__slot {
        font-size: 32px;
    }

    .flip-clock {
        span {
            margin-right: 3px;
        }
    }
}

    @media (max-width: 770px) {
        .no-animation__card {
            font-size: 30px;
        }

        .flip-clock__slot {
            font-size: 30px;
        }
    }

    @media (max-width: 500px) {
        .no-animation__card {
            font-size: 35px;
        }

        .flip-clock__slot {
            font-size: 30px;
        }

        .flip-clock__piece {
            margin: 0;
        }
    }</style>
