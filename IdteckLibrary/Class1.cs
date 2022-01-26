using System;
using System.Threading.Tasks;
using IDTECK.SDK;
using IDTECK.SDK.iEDC.Api;
using IDTECK.SDK.iEDC.Type;
using OdinSdk.BaseLib.Common;
using OdinSdk.BaseLib.Extension;

namespace IdteckLibrary
{
    public class Class1
    {

        public async static void Main()
        {
            await run1();
        }

        public static async Task<string> run1()
        {

            //await changeStatus(Convert.ToByte(1), "19.2.2.1", Convert.ToByte(1), Convert.ToByte(1));
            return "sang";

        }


        public static async Task<RecvType11> run()
        {

            RecvType11 ss = await changeStatus(Convert.ToByte(1), "19.2.2.1", Convert.ToByte(1), Convert.ToByte(1));
            return ss;
            
        }

        public static async Task<RecvType11> changeStatus(byte BoardId, string IpAddress, byte PortNo, byte __encrypt_type)
        {

             iEDCAPI __cedcapi = new iEDCAPI();


            var _class = new SendType11
            {
                port_no = Convert.ToByte(1),
                port_status = Convert.ToByte(1),
                port_type = Convert.ToByte(1)
            };


            return await __cedcapi.InputOutputPortStatusToControllerAsync(BoardId, IpAddress, PortNo, _class, __encrypt_type);
        }
    }
}
