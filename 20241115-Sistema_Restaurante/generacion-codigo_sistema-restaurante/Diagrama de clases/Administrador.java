

/**
 * @version 1.0
 * @created 15-nov.-2024 11:42:56 a. m.
 */
public class Administrador implements IReporteable, IInventariable {

	private int id_administrador;
	private String nombre;
	private String email;

	public Administrador(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 * 
	 * @param ingrediente
	 * @param cantidad
	 */
	public boolean gestionarInventario(String ingrediente, int cantidad){
		return false;
	}

	/**
	 * 
	 * @param ingrediente
	 * @param cantidad
	 */
	public Void gestionarInventario(Ingrediente ingrediente, int cantidad){

	}

	public String generarInformeDiario(){
		return "";
	}

	/**
	 * 
	 * @param fecha
	 */
	public List<Pago> revisarPagos(Date fecha){
		return null;
	}

	/**
	 * 
	 * @param fecha
	 */
	public List<Orden> consultarOrdenes(Date fecha){
		return null;
	}

}