package exam_prep;

public class Professor extends UniversityMember implements LabAccess {
    String department;

    public Professor(String id, String name, String department){
        super(id,name);
        this.department = department;
    }
    @Override
    public String getRole(){
        return "Professor";
    }
    public boolean canLogin(){
        return true;
        
    }
    public int getPrintQuota(){
        return 500;
    }
}
