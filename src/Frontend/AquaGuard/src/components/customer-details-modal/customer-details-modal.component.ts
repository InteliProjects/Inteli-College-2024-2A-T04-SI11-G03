import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { FormsModule } from '@angular/forms';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-customer-details-modal',
  standalone: true,
  imports: [CommonModule, CurrencyPipe, FormsModule],
  templateUrl: './customer-details-modal.component.html',
  styleUrls: ['./customer-details-modal.component.css'],
})
export class CustomerDetailsModalComponent {
  isEditing: boolean = false;

  constructor(
    @Inject(MAT_DIALOG_DATA) public customer: any,
    private dialogRef: MatDialogRef<CustomerDetailsModalComponent>
  ) {}

  saveChanges() {
   
  }

  onClose() {
    Swal.fire({
      title: 'Você tem certeza?',
      text: 'Deseja salvar as alterações?',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#1B7AC3', 
      cancelButtonColor: '#636363', 
      confirmButtonText: 'Sim',
      cancelButtonText: 'Não'
    }).then((result) => {
      if (result.isConfirmed) {
        this.saveChanges();
        Swal.fire({
          title: 'Salvo!',
          text: 'Suas alterações foram salvas com sucesso.',
          icon: 'success',
          confirmButtonText: 'Ok',
          confirmButtonColor: '#1B7AC3'
        }).then(() => {
          this.dialogRef.close();
        });
      } else {
        Swal.fire({
          title: 'Cancelado',
          text: 'Suas alterações não foram salvas.',
          icon: 'error',
          confirmButtonText: 'Ok',
          confirmButtonColor: '#1B7AC3'
        });
      }
    });
  }

  toggleEdit(): void {
    if (this.isEditing) {
      Swal.fire({
        title: 'Cancelar Edição?',
        text: 'Você deseja cancelar as alterações?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#1B7AC3', 
        cancelButtonColor: '#636363', 
        confirmButtonText: 'Sim',
        cancelButtonText: 'Não'
      }).then((result) => {
        if (result.isConfirmed) {
          this.isEditing = false; 
        }
      });
    } else {
      this.isEditing = true;
    }
  }
}
