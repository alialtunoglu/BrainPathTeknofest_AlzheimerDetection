const name: string = "ali";

export default defineEventHandler(() => {
  return {
    hello: name,
  };
});
