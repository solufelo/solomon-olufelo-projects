package exam_prep;

public abstract class UniversityMember implements Comparable<UniversityMember> {


    private String id;
    private String name;

    public UniversityMember(String id, String name){
        if (id == null || id.length() != 9){
            throw new IllegalArgumentException("Invalid Input, Try Again"); 
        }
        this.id = id;
        this.name = name;
    }
    public abstract String getRole();

    public boolean equals(Object obj){
        if (this == obj) return true;
        
        if (obj == null) return false;

        if (obj instanceof UniversityMember){
            UniversityMember other = (UniversityMember) obj;
            return this.id.equals(other.id);
        }
       return false;
    }


    public int compareTo(UniversityMember name){
        return this.id.compareTo(name.id);
    }

    
}