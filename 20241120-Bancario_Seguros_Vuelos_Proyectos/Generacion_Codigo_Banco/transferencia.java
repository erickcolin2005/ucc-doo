

/**
 * @version 1.0
 * @created 22-nov.-2024 6:37:30 a. m.
 */
public class transferencia implements transaccion {

	private int id_transferencia;
	private int id_cuenta_origen;
	private int id_cuenta_destino;
	private double monto;
	private string tipo_transaccion;
	private localdatetime fecha_transaccion;
	public cuenta_ahorro m_cuenta_ahorro;

	public transferencia(){

	}

	public void finalize() throws Throwable {

	}

	public int realizartransaccion(){
		return 0;
	}

}