import { createApp, defineComponent, ref, onMounted } from 'vue'
import { Line, Doughnut } from 'vue-chartjs'
import { Chart, registerables } from 'chart.js'
import './index.css'

Chart.register(...registerables)

const BalanceHistoryChart = defineComponent({
  name: 'BalanceHistoryChart',
  components: { Line },
  props: {
    chartData: { type: Object, required: true },
    chartOptions: { type: Object, required: true }
  },
  template: `<Line :data="chartData" :options="chartOptions" />`
})

const AssetsPieChart = defineComponent({
  name: 'AssetsPieChart',
  components: { Doughnut },
  props: {
    chartData: { type: Object, required: true },
    chartOptions: { type: Object, required: true }
  },
  template: `<Doughnut :data="chartData" :options="chartOptions" />`
})

const DashboardView = defineComponent({
  name: 'DashboardView',
  components: { BalanceHistoryChart, AssetsPieChart },
  setup() {
    const dashboard = ref(null)
    const loading = ref(false)

    const historyData = ref({
      labels: ['J-4', 'J-3', 'J-2', 'J-1', "Aujourd'hui"],
      datasets: [
        {
          label: 'Solde total EUR',
          data: [950, 980, 1020, 1010, 1030],
          borderColor: '#3b82f6',
          backgroundColor: 'rgba(59,130,246,0.2)',
          tension: 0.3
        }
      ]
    })

    const pieData = ref({
      labels: ['BTC', 'ETH', 'AUTRES'],
      datasets: [
        {
          data: [60, 30, 10],
          backgroundColor: ['#f59e0b', '#10b981', '#6366f1']
        }
      ]
    })

    const commonOptions = { responsive: true, maintainAspectRatio: false }

    const fetchDashboard = async () => {
      const token = prompt('Enter your JWT token:')
      if (!token) return
      loading.value = true
      try {
        const res = await fetch('http://localhost:8000/dashboard/', {
          headers: { Authorization: 'Bearer ' + token }
        })
        if (res.ok) {
          dashboard.value = await res.json()
        }
      } catch (err) {
        console.error(err)
      } finally {
        loading.value = false
      }
    }

    onMounted(fetchDashboard)

    return { dashboard, loading, historyData, pieData, commonOptions }
  },
  template: `
    <div>
      <h1 class="text-2xl font-semibold mb-4">Dashboard</h1>
      <div v-if="loading" class="text-center py-6">Chargement...</div>
      <div v-else>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="h-64">
            <BalanceHistoryChart :chart-data="historyData" :chart-options="commonOptions" />
          </div>
          <div class="h-64">
            <AssetsPieChart :chart-data="pieData" :chart-options="commonOptions" />
          </div>
        </div>
        <pre class="mt-4 p-2 bg-gray-100 dark:bg-gray-800 rounded" v-if="dashboard">{{ dashboard }}</pre>
      </div>
    </div>
  `
})

createApp(DashboardView).mount('#app')
