import { Component, AfterViewInit, ElementRef, ViewChild } from '@angular/core';
import { Chart, registerables } from 'chart.js';

@Component({
  selector: 'app-monthly-consumption-graph',
  standalone: true,
  imports: [],
  templateUrl: './monthly-consumption-graph.component.html',
  styleUrls: ['./monthly-consumption-graph.component.css']
})
export class MonthlyConsumptionGraphComponent implements AfterViewInit {
  
  @ViewChild('lineChart') private lineChartRef!: ElementRef<HTMLCanvasElement>;

  value: string | undefined;

  public lineChartData = {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    datasets: [
      {
        data: [65, 59, 80, 81, 56, 55, 40, 70, 60, 90, 85, 100],
        label: 'Consumo',
        fill: false,
      }
    ]
  };

  constructor() {
    Chart.register(...registerables);
  }

  ngAfterViewInit(): void {
    const ctx = this.lineChartRef.nativeElement.getContext('2d');
    if (ctx) {
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.lineChartData.labels,
          datasets: this.lineChartData.datasets
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: false 
            },
            title: {
              display: false,
            }
          },
          scales: {
            x: {
              beginAtZero: true,
              grid: {
                display: false
              }
            },
            y: {
              beginAtZero: true
            }
          }
        }
      });
    } else {
      console.error('Não foi possível obter o contexto do canvas.');
    }
  }
}
