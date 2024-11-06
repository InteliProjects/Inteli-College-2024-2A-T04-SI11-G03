import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 

@Component({
  selector: 'app-upload',
  standalone: true,  
  imports: [CommonModule],
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  fileName: string | null = null;
  isError: boolean = false;
  isCsv: boolean = false;  
  errorMessage: string = '';

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      const file = input.files[0];
      this.fileName = file.name;

      if (file.type !== 'text/csv') {
        this.errorMessage = 'Arquivo inválido ou excede o tamanho suportado.';
        this.isError = true;
        this.isCsv = false; 
        return;
      }

      this.errorMessage = '';
      this.isError = false;
      this.isCsv = true;  

      const reader = new FileReader();
      reader.onload = (e) => {
        const fileContent = e.target?.result;
        console.log(fileContent);
      };
      reader.readAsDataURL(file);
    }
  }

  clearFile(fileInput: HTMLInputElement): void {
    this.fileName = null;
    this.isError = false;
    this.isCsv = false;
    this.errorMessage = '';
    fileInput.value = ''; 
  }

  triggerFileInput(fileInput: HTMLInputElement): void {
    fileInput.click();
  }
}
