import static java.util.Arrays.binarySearch;
import java.util.Locale;
 
 class UDFCountry {
    def static final Set<String> ISO_LANGUAGES = new HashSet<String>
        (Arrays.asList(Locale.getISOLanguages()));
    def static final Set<String> ISO_COUNTRIES = new HashSet<String>
        (Arrays.asList(Locale.getISOCountries()));

    
    def static boolean isValidISOLanguage(String s) {
        return ISO_LANGUAGES.contains(s);
    }

    def static boolean isValidISOCountry(String s) {
        return ISO_COUNTRIES.contains(s);
    }
}