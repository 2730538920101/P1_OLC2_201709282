import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

//INPORTAR COMPONENTES INTENRNOS
import { EditorComponent } from './editor/editor.component';
import { InicioComponent } from './inicio/inicio.component';
import { RouterModule } from '@angular/router';

//IMPORTAR COMPONENTES EXTERNOS
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MONACO_PATH , MonacoEditorModule} from '@materia-ui/ngx-monaco-editor';
//IMPORTAR MODULOS DE ANGULAR MATERIAL
import {MatButtonModule} from '@angular/material/button';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatTabsModule} from '@angular/material/tabs';;
import {MatTableModule} from '@angular/material/table';
import { ErroresComponent } from './errores/errores.component';


@NgModule({
  declarations: [
    InicioComponent,
    EditorComponent,
    ErroresComponent
  ],
  imports: [
    CommonModule,
    MatButtonModule,
    MatGridListModule,
    MatTabsModule,
    BrowserModule,
    FormsModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    MonacoEditorModule,
    MatTableModule,
    RouterModule
  ],
  exports:[
    InicioComponent,
    EditorComponent,
    ErroresComponent,
    RouterModule
  ],
  providers:[
    {
      provide: MONACO_PATH,
      useValue: 'https://unpkg.com/monaco-editor@0.19.3/min/vs'
    }
  ]
})
export class ComponentesModule { }
