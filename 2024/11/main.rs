

fn blink(num:u64, i:u64, depth:u64) -> u64 {
    if i == depth {
        return 1
    }

    if num ==  0 {
        return blink(1, i+1, depth);
    }

    let f = num as f64; 
    let num_digits: u32 = 1 + f.log(10.0).floor() as u32;

    if num_digits % 2 == 1 {
        return blink(num*2024, i+1, depth);
    }

    //println!("{}", num_digits);

    let ten: u64 = 10;
    let t: u64 = ten.pow(num_digits/2);

    //println!("{}", t);

    let right = num % t;
    let left = (num - right)/t;

    
    //println!("{}", left);
    //println!("{}", right);

    return blink(left,i+1,depth) + blink(right,i+1, depth);

}

fn main() {
    let depth = 75;

    let result = 
        blink(3935565, 0, depth) + 
        blink(31753, 0, depth) + 
        blink(437818, 0, depth) + 
        blink(7697, 0, depth) + 
        blink(5, 0, depth) +
        blink(38, 0, depth) +
        blink(0, 0, depth) +
        blink(123, 0, depth);

    println!("{}", result);
}

