import React from "react";
import { ConfigProvider, App } from "antd";

function ThemeProvider({ children }: { children: React.ReactNode }) {
  return <ConfigProvider
  theme={{
    token: {
      colorPrimary: "#1A3636",
      borderRadius: 2,
      controlOutline: "none",
    },
    components: {
      Button: {
        controlHeight: 45,
        
      },
      Input: {
        controlHeight: 45,

      },
    },
  }}
  >
    <App>
      {children}
    </App>
  </ConfigProvider>;
}

export default ThemeProvider;
