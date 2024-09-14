public class Euler1
{
    public static void main(String args[])
    {
        int x = 0;
        int sum = 0;
        while (x < 1000)
        {
            if(x % 3 == 0)
            {
                sum += x;
            }
            else if(x % 5 == 0)
            {
                sum += x;
            }
            x += 1;
        }

        System.out.println(sum);
    }
}