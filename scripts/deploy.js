async function main() {
   const myTPK = await ethers.getContractFactory("myTPK");

   // Start deployment, returning a promise that resolves to a contract object
   const MyTPK = await myTPK.deploy();
   console.log("Contract deployed to address:", MyTPK.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
