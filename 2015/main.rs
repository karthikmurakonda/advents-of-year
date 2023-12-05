fn find_first_negative_index(s: &str) -> Option<usize> {
    let mut count = 0;

    for (i, ch) in s.chars().enumerate() {
        match ch {
            '(' => count += 1,
            ')' => count -= 1,
            _ => return None,
        }

        if count < 0 {
            return Some(i + 1);
        }
    }

    None
}

fn main() {
    let input = include_str!("input.txt");
    println!("Part 1: {}", input.chars().fold(0, |acc, ch| match ch {
        '(' => acc + 1,
        ')' => acc - 1,
        _ => acc,
    }));

    println!("Part 2: {:?}", find_first_negative_index(input));
}