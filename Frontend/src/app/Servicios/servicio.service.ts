import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ServicioService {
  private _errores:Array<String> = new Array();
  constructor(private http:HttpClient) { }

  public post(url:string, body:any):Observable<any>{
    return this.http.post(url,body);
  }
  public setErrores(errores:Array<String>){
    this._errores = errores;
  }

  public getErrores():Array<String>{
    return this._errores;
  }

}