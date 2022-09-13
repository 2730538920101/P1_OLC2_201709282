import { ServicioService } from './../../Servicios/servicio.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-errores',
  templateUrl: './errores.component.html',
  styleUrls: ['./errores.component.css']
})
export class ErroresComponent implements OnInit {
  errores:any[] = [];
  constructor(private servicio:ServicioService) { }

  ngOnInit(): void {
  }

  GenerarTabla(){
    this.errores = this.servicio.getErrores()
  }
}
