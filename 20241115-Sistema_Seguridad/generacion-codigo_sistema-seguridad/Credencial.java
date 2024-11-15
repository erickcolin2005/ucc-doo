package System;


/**
 * @version 1.0
 * @created 15-nov.-2024 9:03:23 a. m.
 */
public class Credencial {

	private int id_credencial;
	private String tipo;
	private String estado;
	public Administrador m_Administrador;

	public Credencial(){

	}

	public void finalize() throws Throwable {

	}

	public boolean activar(){
		return false;
	}

	public boolean revocar(){
		return false;
	}

	/**
	 * 
	 * @param id_credencial
	 */
	public boolean verificarAcceso(int id_credencial){
		return false;
	}

}