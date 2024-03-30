// vitest-globals.d.ts
import { Expect, It, Describe } from 'vitest';

declare global {
  const expect: Expect;
  const describe: Describe;
  const it: It;
  // Declare other global variables from Vitest as needed
}

export {};