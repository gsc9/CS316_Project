import java.util.ArrayList;
import java.util.HashMap;

public abstract class AbstractGen {
	
	protected String myData;
	
	protected abstract String[] extractData();
	
	protected String[] extractMoreData() {
		return null;
	}
	
	protected HashMap<Integer, ArrayList<String>> extractComplexData() {
		return null;
	}
}