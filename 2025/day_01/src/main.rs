use anyhow::{Result, bail};
use utils::read_lines;

fn pt_one() -> Result<()> {
    let mut result = 0;
    let mut cur = 50;
    let lines: Vec<String> = read_lines("day_01/input.txt")?;

    for line in lines {
        let (dir_str, amt_str) = line.split_at(1);

        let dir = match dir_str {
            "L" => -1,
            "R" => 1,
            other => bail!("unexpected direction {other} in line {line:?}"),
        };

        let amt: i32 = amt_str.parse()?;

        cur = (cur + dir * amt).rem_euclid(100);
        if cur == 0 {
            result += 1;
        }
    }

    print!("Part 1 Result: {result}\n");
    Ok(())
}

fn pt_two() -> Result<()> {
    let mut result = 0;
    let mut cur = 50;
    let lines: Vec<String> = read_lines("day_01/input.txt")?;

    for line in lines {
        let (dir_str, amt_str) = line.split_at(1);

        let dir = match dir_str {
            "L" => -1,
            "R" => 1,
            other => bail!("unexpected direction {other} in line {line:?}"),
        };

        let amt: i32 = amt_str.parse()?;

        let laps = amt / 100;
        result += laps;

        if cur != 0 {
            let steps = amt % 100;
            match dir_str {
                "R" if cur + steps >= 100 => result += 1,
                "L" if steps >= cur => result += 1,
                _ => {}
            }
        }

        cur = (cur + dir * amt).rem_euclid(100);

        // println!("{prev} -> {dir} {amt} -> {cur} = {result} (+{overflow})");
    }

    print!("Part 2 Result: {result}\n");
    Ok(())
}

fn main() -> Result<()> {
    pt_one()?;
    pt_two()?;
    Ok(())
}
